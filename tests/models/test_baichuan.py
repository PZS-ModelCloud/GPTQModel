from model_test import ModelTest

class TestBaiChuan(ModelTest):
    NATIVE_MODEL_ID = "baichuan-inc/Baichuan2-7B-Chat"
    NATIVE_ARC_CHALLENGE_ACC = 0.4104
    NATIVE_ARC_CHALLENGE_ACC_NORM = 0.4317
    QUANT_ARC_MAX_NEGATIVE_DELTA = 0.02
    QUANT_ARC_MAX_POSITIVE_DELTA = 0.05
    def test_baichuan(self):
        model, tokenizer = self.quantModel(self.NATIVE_MODEL_ID, trust_remote_code=True)
        
        task_results = self.lm_eval(model, trust_remote_code=True)
        for filter, value in task_results.items():
            per = self.calculatorPer(filter=filter, value=value)
            self.assertTrue(90 <= per <= 110,
                            f"{filter}: {value} diff {per:.2f}% is out of the expected range (90%-110%)")
