

# Class al::ActorPoseKeeperTRSV



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**ActorPoseKeeperTRSV**](classal_1_1_actor_pose_keeper_t_r_s_v.md)





* `#include <alActorPoseKeeper.h>`



Inherits the following classes: [al::ActorPoseKeeperBase](classal_1_1_actor_pose_keeper_base.md)




























## Public Static Attributes inherited from al::ActorPoseKeeperBase

See [al::ActorPoseKeeperBase](classal_1_1_actor_pose_keeper_base.md)

| Type | Name |
| ---: | :--- |
|  [**const**](classal_1_1_functor_v0_m.md) sead::Vector3f | [**sDefaultGravity**](classal_1_1_actor_pose_keeper_base.md#variable-sdefaultgravity)  <br> |


























## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**ActorPoseKeeperTRSV**](#function-actorposekeepertrsv) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**calcBaseMtx**](#function-calcbasemtx) (sead::Matrix34f \* out) <br> |
| virtual [**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & | [**getRotate**](#function-getrotate) () const<br> |
| virtual sead::Vector3f \* | [**getRotatePtr**](#function-getrotateptr) () <br> |
| virtual [**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & | [**getScale**](#function-getscale) () const<br> |
| virtual sead::Vector3f \* | [**getScalePtr**](#function-getscaleptr) () <br> |
| virtual [**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & | [**getVelocity**](#function-getvelocity) () const<br> |
| virtual sead::Vector3f \* | [**getVelocityPtr**](#function-getvelocityptr) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**updatePoseMtx**](#function-updateposemtx) ([**const**](classal_1_1_functor_v0_m.md) sead::Matrix34f \* mtx) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**updatePoseQuat**](#function-updateposequat) ([**const**](classal_1_1_functor_v0_m.md) sead::Quatf & quat) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**updatePoseRotate**](#function-updateposerotate) ([**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & rot) <br> |


## Public Functions inherited from al::ActorPoseKeeperBase

See [al::ActorPoseKeeperBase](classal_1_1_actor_pose_keeper_base.md)

| Type | Name |
| ---: | :--- |
|   | [**ActorPoseKeeperBase**](classal_1_1_actor_pose_keeper_base.md#function-actorposekeeperbase) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**calcBaseMtx**](classal_1_1_actor_pose_keeper_base.md#function-calcbasemtx) (sead::Matrix34f \* out) = 0<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**copyPose**](classal_1_1_actor_pose_keeper_base.md#function-copypose) ([**const**](classal_1_1_functor_v0_m.md) [**ActorPoseKeeperBase**](classal_1_1_actor_pose_keeper_base.md) \* from) <br> |
| virtual [**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & | [**getFront**](classal_1_1_actor_pose_keeper_base.md#function-getfront) () const<br> |
| virtual sead::Vector3f \* | [**getFrontPtr**](classal_1_1_actor_pose_keeper_base.md#function-getfrontptr) () <br> |
| virtual [**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & | [**getGravity**](classal_1_1_actor_pose_keeper_base.md#function-getgravity) () const<br> |
| virtual sead::Vector3f \* | [**getGravityPtr**](classal_1_1_actor_pose_keeper_base.md#function-getgravityptr) () <br> |
| virtual [**const**](classal_1_1_functor_v0_m.md) sead::Quatf & | [**getQuat**](classal_1_1_actor_pose_keeper_base.md#function-getquat) () const<br> |
| virtual sead::Quatf \* | [**getQuatPtr**](classal_1_1_actor_pose_keeper_base.md#function-getquatptr) () <br> |
| virtual [**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & | [**getRotate**](classal_1_1_actor_pose_keeper_base.md#function-getrotate) () const<br> |
| virtual sead::Vector3f \* | [**getRotatePtr**](classal_1_1_actor_pose_keeper_base.md#function-getrotateptr) () <br> |
| virtual [**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & | [**getScale**](classal_1_1_actor_pose_keeper_base.md#function-getscale) () const<br> |
| virtual sead::Vector3f \* | [**getScalePtr**](classal_1_1_actor_pose_keeper_base.md#function-getscaleptr) () <br> |
|  [**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & | [**getTrans**](classal_1_1_actor_pose_keeper_base.md#function-gettrans) () const<br> |
|  sead::Vector3f \* | [**getTransPtr**](classal_1_1_actor_pose_keeper_base.md#function-gettransptr) () <br> |
| virtual [**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & | [**getVelocity**](classal_1_1_actor_pose_keeper_base.md#function-getvelocity) () const<br> |
| virtual sead::Vector3f \* | [**getVelocityPtr**](classal_1_1_actor_pose_keeper_base.md#function-getvelocityptr) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**updatePoseMtx**](classal_1_1_actor_pose_keeper_base.md#function-updateposemtx) ([**const**](classal_1_1_functor_v0_m.md) sead::Matrix34f \* mtx) = 0<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**updatePoseQuat**](classal_1_1_actor_pose_keeper_base.md#function-updateposequat) ([**const**](classal_1_1_functor_v0_m.md) sead::Quatf & quat) = 0<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**updatePoseRotate**](classal_1_1_actor_pose_keeper_base.md#function-updateposerotate) ([**const**](classal_1_1_functor_v0_m.md) sead::Vector3f & rot) = 0<br> |






















































## Public Functions Documentation




### function ActorPoseKeeperTRSV 

```C++
al::ActorPoseKeeperTRSV::ActorPoseKeeperTRSV () 
```




<hr>



### function calcBaseMtx 

```C++
virtual void al::ActorPoseKeeperTRSV::calcBaseMtx (
    sead::Matrix34f * out
) 
```



Implements [*al::ActorPoseKeeperBase::calcBaseMtx*](classal_1_1_actor_pose_keeper_base.md#function-calcbasemtx)


<hr>



### function getRotate 

```C++
virtual const sead::Vector3f & al::ActorPoseKeeperTRSV::getRotate () const
```



Implements [*al::ActorPoseKeeperBase::getRotate*](classal_1_1_actor_pose_keeper_base.md#function-getrotate)


<hr>



### function getRotatePtr 

```C++
virtual sead::Vector3f * al::ActorPoseKeeperTRSV::getRotatePtr () 
```



Implements [*al::ActorPoseKeeperBase::getRotatePtr*](classal_1_1_actor_pose_keeper_base.md#function-getrotateptr)


<hr>



### function getScale 

```C++
virtual const sead::Vector3f & al::ActorPoseKeeperTRSV::getScale () const
```



Implements [*al::ActorPoseKeeperBase::getScale*](classal_1_1_actor_pose_keeper_base.md#function-getscale)


<hr>



### function getScalePtr 

```C++
virtual sead::Vector3f * al::ActorPoseKeeperTRSV::getScalePtr () 
```



Implements [*al::ActorPoseKeeperBase::getScalePtr*](classal_1_1_actor_pose_keeper_base.md#function-getscaleptr)


<hr>



### function getVelocity 

```C++
virtual const sead::Vector3f & al::ActorPoseKeeperTRSV::getVelocity () const
```



Implements [*al::ActorPoseKeeperBase::getVelocity*](classal_1_1_actor_pose_keeper_base.md#function-getvelocity)


<hr>



### function getVelocityPtr 

```C++
virtual sead::Vector3f * al::ActorPoseKeeperTRSV::getVelocityPtr () 
```



Implements [*al::ActorPoseKeeperBase::getVelocityPtr*](classal_1_1_actor_pose_keeper_base.md#function-getvelocityptr)


<hr>



### function updatePoseMtx 

```C++
virtual void al::ActorPoseKeeperTRSV::updatePoseMtx (
    const sead::Matrix34f * mtx
) 
```



Implements [*al::ActorPoseKeeperBase::updatePoseMtx*](classal_1_1_actor_pose_keeper_base.md#function-updateposemtx)


<hr>



### function updatePoseQuat 

```C++
virtual void al::ActorPoseKeeperTRSV::updatePoseQuat (
    const sead::Quatf & quat
) 
```



Implements [*al::ActorPoseKeeperBase::updatePoseQuat*](classal_1_1_actor_pose_keeper_base.md#function-updateposequat)


<hr>



### function updatePoseRotate 

```C++
virtual void al::ActorPoseKeeperTRSV::updatePoseRotate (
    const sead::Vector3f & rot
) 
```



Implements [*al::ActorPoseKeeperBase::updatePoseRotate*](classal_1_1_actor_pose_keeper_base.md#function-updateposerotate)


<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/LiveActor/alActorPoseKeeper.h`

