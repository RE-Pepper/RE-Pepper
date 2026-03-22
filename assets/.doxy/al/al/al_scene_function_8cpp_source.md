

# File alSceneFunction.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Scene**](dir_9ee5e72b41628d4cc49af8432465a4be.md) **>** [**alSceneFunction.cpp**](al_scene_function_8cpp.md)

[Go to the documentation of this file](al_scene_function_8cpp.md)


```C++
#include <Factory/alActorFactory.h>
#include <LiveActor/alActorInitInfo.h>
#include <LiveActor/alActorInitUtil.h>
#include <Placement/alPlacementFunction.h>
#include <Scene/alSceneFunction.h>

namespace al
{

#ifdef NON_MATCHING
// WIP
void initPlacementMap( Scene* scene, const Resource* stageArchive, const ActorInitInfo& infoTemplate, const char* infoIterName )
{
        PlacementInfo infoIter;
        if ( tryGetPlacementInfo( &infoIter, stageArchive, infoIterName ) && scene->getActorFactory() )
        {
                int size = infoIter.getSize();
                for ( int i = 0; i < size; i++ )
                {
                        PlacementInfo placementInfo;
                        infoIter.tryGetIterByIndex( &placementInfo, i );
                        const char* objectName = nullptr;
                        if ( al::tryGetObjectName( &objectName, placementInfo ) )
                        {
                                al::CreateActorFuncPtr create = scene->getActorFactory()->getCreator( objectName );
                                if ( create )
                                {
                                        ActorInitInfo info;
                                        info.initNew( &placementInfo, infoTemplate );
                                        LiveActor* actor = create( objectName );
                                        al::initCreateActorWithPlacementInfo( actor, info );
                                }
                        }
                }
        }
}
#endif

bool tryGetPlacementInfo( PlacementInfo* out, const Resource* stageArchive, const char* infoIterName )
{
        if ( !stageArchive )
                return false;
        if ( stageArchive )
        {
                const u8* stageData = stageArchive->getByml( "StageData" );
                ByamlIter stageDataByaml( stageData );
                ByamlIter allInfosIter;
                if ( stageDataByaml.tryGetIterByKey( &allInfosIter, "AllInfos" ) )
                {
                        ByamlIter unused;
                        if ( allInfosIter.tryGetIterByKey( out, infoIterName ) )
                                return true;
                }
                else
                        return false;
        }
}

} // namespace al
```


