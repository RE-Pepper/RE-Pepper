#pragma once

#include <Placement/alPlacementInfo.h>
#include <Resource/alResource.h>
#include <Scene/alScene.h>

namespace al
{
class Resource;
class Scene;

void initPlacementMap( Scene* scene, const Resource* stageArchive, const ActorInitInfo& infoTemplate, const char* infoIterName );

bool tryGetPlacementInfo( PlacementInfo* out, const Resource* stageArchive, const char* infoIterName );

} // namespace al
