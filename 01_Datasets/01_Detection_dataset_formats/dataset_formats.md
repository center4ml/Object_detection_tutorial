# Dataset annotation formats

Object detection datasets consist of 1) images 2) annotations. Annotations are stored in text files which inform where the instances are located in each image. They also contain information about category of instance and may also store additional informations, such as image size, license etc.

## What annotations must contain?

- bounding boxes
- categories of instances


## Main types of annotations

Three main formats of annotations:
1. COCO
1. YOLO
1. Pascal VOC

named after datasets (COCO, Pascal) or algoritm (YOLO) for which the formats were introduced.

Currently, YOLO family of detectors requires YOLO format, while most of other solutions can use both COCO or Pascal formats. 

In this tutorial, we will cover YOLO and COCO formats, leaving Pascal aside.

Datsets can be converted between different formats

## Main differences


## COCO

Great and informative descriptions are [here](https://www.immersivelimit.com/tutorials/create-coco-annotations-from-scratch)

## YOLO


## Conversion between formats

1. COCO -> YOLO: notebook coco2yolo.ipynb
1. YOLO -> COCO: [code](https://github.com/qwirky-yuzu/COCO-to-YOLO) [blog](https://medium.com/@thamqianyu96/coco-to-yolo-annotations-9d638bb3eb4f)