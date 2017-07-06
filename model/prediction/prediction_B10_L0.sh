source ../config/exportVariable.sh
cd $SEQ2SEQ_DIR

CUDA_VISIBLE_DEVICES=`/opt/Tools/bin/first-free-gpu|head -1` python -m bin.infer \
  --tasks "
    - class: DecodeText
      params:
        delimiter: ''
    - class: DumpBeams
      params:
        file: ${PRED_DIR}/beams_10.npz" \
  --model_dir $MODEL_DIR \
  --model_params "
    inference.beam_search.beam_width: 10" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_delimiter: ''
      target_delimiter: ''
      source_files:
        - $TEST_SOURCES" \
  > ${PRED_DIR}/predictions_B10.txt
./bin/tools/multi-bleu.perl ${DEV_TARGETS_REF} < ${PRED_DIR}/predictions_B10.txt > ${PRED_DIR}/results_B10.txt

cd $CODE_DIR