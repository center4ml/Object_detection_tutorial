# explicitly over-write all the `num_classes` field from default 80 to number of classes in the dataset
num_classes=5
model = dict(
    panoptic_head=dict(
        num_things_classes=num_classes,
        num_stuff_classes=0,
        loss_cls=dict(class_weight=[1.0] * num_classes + [0.1])),
    panoptic_fusion_head=dict(
        num_things_classes=num_classes,
        num_stuff_classes=0),
    test_cfg=dict(panoptic_on=False)
    )



