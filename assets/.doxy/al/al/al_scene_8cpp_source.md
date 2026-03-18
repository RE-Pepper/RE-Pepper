

# File alScene.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Scene**](dir_ca634763a19f7100b987afb79dcab1e3.md) **>** [**alScene.cpp**](al_scene_8cpp.md)

[Go to the documentation of this file](al_scene_8cpp.md)


```C++
#include <Factory/alActorFactory.h>
#include <LiveActor/alActorInitInfo.h>
#include <Scene/SceneObjFactory.h>
#include <Scene/alScene.h>
#include <Scene/alSceneObjHolder.h>
#include <Stage/alStageResourceKeeper.h>
#include <System/Application.h>

namespace al
{

Scene::Scene( const char* name )
    : NerveExecutor( name ), mAudioKeeper( nullptr ), mLiveActorKit( nullptr ), mLayoutKit( nullptr ),
      mSceneObjHolder( nullptr ), mActorFactory( nullptr ), _20( nullptr ), mResourceKeeper( nullptr ),
      _28( nullptr ), _2C( nullptr ), mIsAlive( false )
{
}

void Scene::appear()
{
        if ( !mIsAlive )
                mIsAlive = true;
}

void Scene::kill()
{
        mIsAlive = false;
}

#ifdef NON_MATCHING
void Scene::movement()
{
        if ( mIsAlive )
        {
                updateNerve();
                control();
                if ( mAudioKeeper )
                        mAudioKeeper->update();
        }
}
#endif

void Scene::control()
{
}

AudioKeeper* Scene::getAudioKeeper() const
{
        return mAudioKeeper;
}

#ifdef NON_MATCHING
void Scene::initAndLoadStageResource( const char* stageName, int scenario, sead::Heap* heap )
{
        mResourceKeeper = new StageResourceKeeper;
        mResourceKeeper->initAndLoadResource( stageName, scenario, heap );
}
#endif

void Scene::initActorFactory()
{
        mActorFactory = new ActorFactory();
}

void Scene::initSceneObjHolder()
{
        SceneObjHolder* holder = SceneObjFactory::createSceneObjHolder();
        mSceneObjHolder        = holder;
        Application::instance()->setSceneObjHolder( holder );
}

void Scene::endInit( const ActorInitInfo& info )
{
        if ( mSceneObjHolder )
                mSceneObjHolder->initAfterPlacementSceneObj( info );
}

} // namespace al
```


