source ../config/exportVariable.sh


export BEAM_CODE_DIR=${CODE_DIR}/beamCode/
export BEAM_OUTPUT_DIR=${PRED_DIR}/beamResults/
export NUM_DIALOGUE=4673

cd ${BEAM_CODE_DIR}
python ${BEAM_CODE_DIR}/beamDecoder.py --beamFile=${PRED_DIR}/beams_20_withPenalty.npz --vocabFile=${VOCAB_TARGET} --numDialogue=$NUM_DIALOGUE --outputFile=${BEAM_OUTPUT_DIR}/beam_20_LP1_Full_BLEU.pkl 

python ${BEAM_CODE_DIR}/writeBestBeamResultForBLEU.py --pickleFilePath=${BEAM_OUTPUT_DIR}/beam_20_LP1_Full_BLEU.pkl --outputFile=${PRED_DIR}/predictions_beam_20_LP1_Full_BLEU.txt 


cd $SEQ2SEQ_DIR
./bin/tools/multi-bleu.perl ${DEV_TARGETS_REF} < ${PRED_DIR}/predictions_beam_20_LP1_Full_BLEU.txt > ${PRED_DIR}/results_beam_20_LP1_Full_BLEU.txt
cd $CODE_DIR