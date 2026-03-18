

# Class al::RailRider



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**RailRider**](classal_1_1_rail_rider.md)





* `#include <alRailRider.h>`





































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**RailRider**](#function-railrider) ([**Rail**](classal_1_1_rail.md) \* rail) <br> |
|  [**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & | [**getCurrentDir**](#function-getcurrentdir) () const<br> |
|  [**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & | [**getCurrentPos**](#function-getcurrentpos) () const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isLoop**](#function-isloop) () const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isReachedGoal**](#function-isreachedgoal) () const<br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**moveToNearestRail**](#function-movetonearestrail) ([**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & r1) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**moveToRailStart**](#function-movetorailstart) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**setSpeed**](#function-setspeed) ([**float**](classal_1_1_functor_v0_m.md) speed) <br> |




























## Public Functions Documentation




### function RailRider 

```C++
al::RailRider::RailRider (
    Rail * rail
) 
```




<hr>



### function getCurrentDir 

```C++
inline const sead::Vector3f & al::RailRider::getCurrentDir () const
```




<hr>



### function getCurrentPos 

```C++
inline const sead::Vector3f & al::RailRider::getCurrentPos () const
```




<hr>



### function isLoop 

```C++
inline bool al::RailRider::isLoop () const
```




<hr>



### function isReachedGoal 

```C++
bool al::RailRider::isReachedGoal () const
```




<hr>



### function moveToNearestRail 

```C++
void al::RailRider::moveToNearestRail (
    const sead::Vector3f & r1
) 
```




<hr>



### function moveToRailStart 

```C++
void al::RailRider::moveToRailStart () 
```




<hr>



### function setSpeed 

```C++
inline void al::RailRider::setSpeed (
    float speed
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/include/Rail/alRailRider.h`

