

# File alSceneObjHolder.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Scene**](dir_9ee5e72b41628d4cc49af8432465a4be.md) **>** [**alSceneObjHolder.cpp**](al_scene_obj_holder_8cpp.md)

[Go to the documentation of this file](al_scene_obj_holder_8cpp.md)


```C++
#include <LiveActor/alActorInitInfo.h>
#include <Scene/alISceneObj.h>
#include <Scene/alSceneObjHolder.h>
#include <System/Application.h>

namespace al
{

#pragma no_inline // probably belongs in another file

SceneObjHolder* getSceneObjHolder()
{
        return al::getApplication()->getSceneObjHolder();
}

ISceneObj* SceneObjHolder::getObj( int id ) const
{
        return mObjs[ id ];
}

bool SceneObjHolder::isExist( int id ) const
{
        return mObjs[ id ] != nullptr;
}

void SceneObjHolder::setObj( ISceneObj* obj, int id )
{
        mObjs[ id ] = obj;
}

ISceneObj* SceneObjHolder::create( int id )
{
        if ( mObjs[ id ] == nullptr )
        {
                ISceneObj* newObj = mCreateFunc( id );
                mObjs[ id ]       = newObj;
                newObj->initSceneObj();
        }
        return mObjs[ id ];
}

void SceneObjHolder::initAfterPlacementSceneObj( const ActorInitInfo& info )
{
        for ( int i = 0; i < mSize; i++ )
                if ( mObjs[ i ] )
                        mObjs[ i ]->initAfterPlacementSceneObj( info );
}

ISceneObj* createSceneObj( int id )
{
        return getSceneObjHolder()->create( id );
}

ISceneObj* getSceneObj( int id )
{
        return getSceneObjHolder()->getObj( id );
}

bool isExistSceneObj( int id )
{
        return getSceneObjHolder()->isExist( id );
}

void setSceneObj( ISceneObj* obj, int id )
{
        return getSceneObjHolder()->setObj( obj, id );
}

} // namespace al
```


