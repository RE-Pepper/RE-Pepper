

# Class al::AreaShape



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**AreaShape**](classal_1_1_area_shape.md)





* `#include <alAreaShape.h>`





Inherited by the following classes: [al::AreaShapeCube](classal_1_1_area_shape_cube.md)
































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**AreaShape**](#function-areashape) () <br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**calcLocalPos**](#function-calclocalpos) (sead::Vector3f \* out, [**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & trans) const<br> |
| virtual [**bool**](classal_1_1_functor_v0_m.md) | [**isInVolume**](#function-isinvolume) ([**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & trans) const = 0<br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**setBaseMtxPtr**](#function-setbasemtxptr) ([**const**](classal_1_1_functor_v0_m.md) sead::Matrix34f \* baseMtxPtr) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**setScale**](#function-setscale) ([**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & scale) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v1**](#function-v1) () = 0<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v2**](#function-v2) () = 0<br> |




























## Public Functions Documentation




### function AreaShape 

```C++
al::AreaShape::AreaShape () 
```




<hr>



### function calcLocalPos 

```C++
bool al::AreaShape::calcLocalPos (
    sead::Vector3f * out,
    const sead::Vector3f & trans
) const
```




<hr>



### function isInVolume 

```C++
virtual bool al::AreaShape::isInVolume (
    const sead::Vector3f & trans
) const = 0
```




<hr>



### function setBaseMtxPtr 

```C++
inline void al::AreaShape::setBaseMtxPtr (
    const sead::Matrix34f * baseMtxPtr
) 
```




<hr>



### function setScale 

```C++
void al::AreaShape::setScale (
    const sead::Vector3f & scale
) 
```




<hr>



### function v1 

```C++
virtual void al::AreaShape::v1 () = 0
```




<hr>



### function v2 

```C++
virtual void al::AreaShape::v2 () = 0
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/AreaObj/alAreaShape.h`

