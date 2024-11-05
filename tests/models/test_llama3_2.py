from model_test import ModelTest

class TestLlama3_2(ModelTest):
    NATIVE_MODEL_ID = "meta-llama/Llama-3.2-1B-Instruct"
    NATIVE_ARC_CHALLENGE_ACC = 0.3567
    NATIVE_ARC_CHALLENGE_ACC_NORM = 0.3805

    def test_llama3_2(self):
        model, tokenizer = self.quantModel(self.NATIVE_MODEL_ID)

        task_results = self.lm_eval(model, trust_remote_code=True)
        for filter, value in task_results.items():
            per = self.calculatorPer(filter=filter, value=value)
            self.assertTrue(90 <= per <= 110,
                            f"{filter}: {value} diff {per:.2f}% is out of the expected range (90%-110%)")
