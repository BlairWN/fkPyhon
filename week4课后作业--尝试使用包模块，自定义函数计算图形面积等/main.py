#!/usr/bin/env python
# coding: utf-8

# In[18]:


#使用如下包与模块结构，计算几种常见平面和3D图形的面积、表面积与体积，
#1、面积
from geometry.area import square,circle,rectangle,triangles
print(square.superfacial(2))#正方形
print(circle.superfacial(2))#圆形
print(rectangle.superfacial(2,3))#长方形
print(triangles.superfacial(2,3))#三角形


# In[19]:


#2、表面积
from geometry.surface_area import cube,cuboid,cylinder,sphere
print(cube.superf(2))#正方体积
print(cuboid.superf(2,3,4))#长方体
print(cylinder.superf(2,3))#圆柱体
print(sphere.superf(2))#球体


# In[20]:


#3、体积
from geometry.volume import cube,cuboid,cylinder,sphere
print(cube.vol(2))#正方体积
print(cuboid.vol(2,3,4))#长方体
print(cylinder.vol(2,3))#圆柱体
print(sphere.vol(2))#球体

