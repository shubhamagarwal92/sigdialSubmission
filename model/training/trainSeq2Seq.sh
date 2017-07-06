source ../config/exportVariable.sh
cd $SEQ2SEQ_DIR
CUDA_VISIBLE_DEVICES=`/opt/Tools/bin/first-free-gpu|head -1` python -m bin.train \
  --config_paths="
      $CODE_DIR/training/nmt_medium.yml,
      $CODE_DIR/training/train_seq2seq.yml,
      $CODE_DIR/training/text_metrics_bpe.yml" \
  --model_params "
      vocab_source: $VOCAB_SOURCE
      vocab_target: $VOCAB_TARGET" \
  --input_pipeline_train "
    class: ParallelTextInputPipeline
    params:
      source_delimiter: ''
      target_delimiter: ''
      source_files:
        - $TRAIN_SOURCES
      target_files:
        - $TRAIN_TARGETS" \
  --input_pipeline_dev "
    class: ParallelTextInputPipeline
    params:
      source_delimiter: ''
      target_delimiter: ''
      source_files:
        - $DEV_SOURCES
      target_files:
        - $DEV_TARGETS" \
  --batch_size 32 \
  --train_steps $TRAIN_STEPS \
  --output_dir $MODEL_DIR

cd $CODE_DIR/training