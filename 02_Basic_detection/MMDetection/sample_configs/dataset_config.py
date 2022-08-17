# 1. dataset settings
dataset_type = 'CocoDataset'
classes = ('Chardonnay', 'Cabernet Franc', 'Cabernet Sauvignon', 'Sauvignon Blanc', 'Syrah')
num_classes = len(classes)
data_root = '/scratch/projects/023/wprawka_01/data/wgisd'

data = dict(
    train=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        data_root = data_root,
        ann_file='coco_annotations/train_polygons_instances.json',
        img_prefix='data'),
    val=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        data_root = data_root,
        ann_file='coco_annotations/test_polygons_instances.json',
        img_prefix='data'),
    test=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        data_root = data_root,
        ann_file='coco_annotations/test_polygons_instances.json',
        img_prefix='data'))


