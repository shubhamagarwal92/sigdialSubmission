source ../config/exportVariable.sh
cd $SEQ2SEQ_DIR

CUDA_VISIBLE_DEVICES=`/opt/Tools/bin/first-free-gpu|head -1` python -m bin.infer \
  --tasks "
    - class: DecodeText
      params:
        delimiter: ''
        unk_replace: True"\
  --model_dir $MODEL_DIR \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_delimiter: ''
      target_delimiter: ''
      source_files:
        - $TEST_SOURCES" \
  >  ${PRED_DIR}/predictions_greedy.txt

./bin/tools/multi-bleu.perl ${DEV_TARGETS_REF} < ${PRED_DIR}/predictions_greedy.txt > ${PRED_DIR}/results_greedy.txt
cd $CODE_DIR