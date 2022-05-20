optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
        policy='step',
        warmup='linear',
        warmup_iters=100,
        warmup_ratio=0.001,
        step=[8])

log_config = dict(
           interval=100,
           # hooks=[dict(type='TensorboardLoggerHook')]
            )

#checkpoint_config = dict(interval=1)
runner = dict(max_epochs=10)

