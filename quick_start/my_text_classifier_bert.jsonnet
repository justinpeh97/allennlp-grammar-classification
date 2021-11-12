local bert_model = "bert-base-uncased";

{
    "dataset_reader" : {
        "type": "classification-tsv",
        "tokenizer": {
            "type": "pretrained_transformer",
            "model_name": bert_model,
        },
        "token_indexers": {
            "bert": {
                "type": "pretrained_transformer",
                "model_name": bert_model,
            }
        },
        "max_tokens": 512
    },
    "train_data_path": "/kaggle/working/allennlp-guide/quick_start/data/gec/fce.train.gold.bea19.txt",
    "validation_data_path": "/kaggle/working/allennlp-guide/quick_start/data/gec/fce.dev.gold.bea19.txt",
    "model": {
        "type": "simple_classifier",
        "embedder": {
            "token_embedders": {
                "bert": {
                    "type": "pretrained_transformer",
                    "model_name": bert_model
                }
            }
        },
        "encoder": {
            "type": "bert_pooler",
            "pretrained_model": bert_model,
            "requires_grad": true
        }
    },
    "data_loader": {
        "batch_size": 8,
        "shuffle": true
    },
    "trainer": {
        "optimizer": {
            "type": "huggingface_adamw",
            "lr": 1.0e-5
        },
        "num_epochs": 5,
		"cuda_device":0
    }
}
