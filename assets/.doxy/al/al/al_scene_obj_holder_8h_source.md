

# File alSceneObjHolder.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Scene**](dir_bbf0d395114b7d01e47e296975854f01.md) **>** [**alSceneObjHolder.h**](al_scene_obj_holder_8h.md)

[Go to the documentation of this file](al_scene_obj_holder_8h.md)


```C++
#pragma once

namespace al
{
class ActorInitInfo;
class ISceneObj;

class SceneObjHolder
{
private:
        typedef ISceneObj* ( *CreateFunc )( int id );

        CreateFunc  mCreateFunc;
        ISceneObj** mObjs;
        int         mSize;

public:
        ISceneObj* create( int id );
        ISceneObj* getObj( int id ) const;
        bool       isExist( int id ) const;
        void       setObj( ISceneObj* obj, int id );

        void initAfterPlacementSceneObj( const ActorInitInfo& info );

public:
        SceneObjHolder( CreateFunc func, int size );
};

SceneObjHolder* getSceneObjHolder();
ISceneObj*      createSceneObj( int id );
ISceneObj*      getSceneObj( int id );
bool            isExistSceneObj( int id );
void            setSceneObj( ISceneObj* obj, int id );

} // namespace al
```


