# Trees
Trees are a data structure with nodes that contain a value and links to other nodes that contain a relation ship to that value. 

## Binary Tree
Figure 1 below shows just one type of a tree, a binary. In this image each node (circles) can have up to 3 links (black arrows). 2 links of each node can be to there child, while 1 can be to there parent. All nodes that are linked to a child node are considered parents, even if they are the child of another node. The leaf node are the ones with no children. The tree represented in this image is a binary tree because it contains nodes that have no more than 2 children, one child that is "less" and one child that is "more." Less and more is important because it means that to find a value in a tree you can start at the root and then compare the value to the node value, if the value you're looking for is more that the load value you can do the same comparison on it's right child, or it's left child if the value is less. By doing this until you value equals the node value, or there is no child, you can efficiently check or add values without checking every element.

![Figure 1](pictures/trees_1.png)
*Figure 1 (from alytech.com)*

## definitions

* __Root Node__ - The only node with no parent.
* __Parent Node__ - Any node with a child.
* __Child Node__ - A node that is linked to a parent node.
* __Leaf Node__ - A node with no children.

## Example



## Problem for you to Solve

Using both sets and a tree, make conflict resolution more efficient than possible using only sets.