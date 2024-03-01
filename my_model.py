from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline


def check_phishing(text):
    # Path to the directory where you've uploaded your model and tokenizer files
    model_dir = "/home/rpg1/mysite/Phishing-Detection-App/Flask App/tinyBERT"
    # you can load your model and tokenizer like this:
    model = AutoModelForSequenceClassification.from_pretrained(model_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)
    result = pipe(text)


    res = pipe(text)
    return res
