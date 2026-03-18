

# File alSceneObjHolder.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Scene**](dir_ca634763a19f7100b987afb79dcab1e3.md) **>** [**alSceneObjHolder.cpp**](al_scene_obj_holder_8cpp.md)

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


