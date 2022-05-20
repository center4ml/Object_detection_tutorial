# 1. dataset settings
# this config is for the dataset from https://public.roboflow.com/object-detection/chess-full
dataset_type = 'CocoDataset'
classes = ('pieces', 'bishop', 'black-bishop', 'black-king', 'black-knight', 'black-pawn', 'black-queen', 'black-rook', 'white-bishop', 'white-king', 'white-knight', 'white-pawn', 'white-queen', 'white-rook')
num_classes = len(classes)
data_root = '/home/username/data/ChessPiecesv24'

data = dict(
    samples_per_gpu=8,
    workers_per_gpu=8,
    train=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        data_root = data_root,
        ann_file='annotations/instances_train.json',
        img_prefix='train'),
    val=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        data_root = data_root,
        ann_file='annotations/instances_val.json',
        img_prefix='val'),
    test=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        data_root = data_root,
        ann_file='annotations/instances_test.json',
        img_prefix='test'))

# 2. model settings

# explicitly over-write all the `num_classes` field from default 80 to 5.
model = dict(roi_head=dict(bbox_head=dict(num_classes=num_classes)))


work_dir = './mmdet_outupt/chess_02'

