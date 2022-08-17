data=dict(
    workers_per_gpu=6,
    train_dataloader=dict(samples_per_gpu=6),
    val_dataloader=dict(samples_per_gpu=1),
    test_dataloader=dict(samples_per_gpu=1)
    )

