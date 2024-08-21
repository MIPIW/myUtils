class ModelUtils:
    def __init__(self):
        pass

    @staticmethod
    def load_model_to_device(
        *,
        model_checkpoint,
        model_loading_class,
        tokenizer_loading_class,
        tokenizer_checkpoint=None,
        # to_gpu=True,
        quantization_config=None,
    ):
        import torch

        if quantization_config is None:
            model = model_loading_class.from_pretrained(
                model_checkpoint,
                attn_implementation="flash_attention_2",
                device_map="auto",
            )
            model.half()

        else:
            model = model_loading_class.from_pretrained(
                model_checkpoint,
                device_map="auto",
                quantization_config=quantization_config,
            )

        count_params = sum(p.numel() for p in model.parameters())
        print("Total Parameters: ", "{:,}".format(count_params))

        if tokenizer_checkpoint is None:
            tokenizer = tokenizer_loading_class.from_pretrained(model_checkpoint)
        else:
            tokenizer = tokenizer_loading_class.from_pretrained(tokenizer_checkpoint)

        # device_map = 'auto' deals with it
        # device = "cuda" if (to_gpu == True) and torch.cuda.is_available() else "cpu"
        # model.to(device)

        return model, tokenizer
