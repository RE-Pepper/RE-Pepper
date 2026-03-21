

# File alAreaObjFactory.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Factory**](dir_bf7711d79db7f41a859fc1cca3bfc2af.md) **>** [**alAreaObjFactory.cpp**](al_area_obj_factory_8cpp.md)

[Go to the documentation of this file](al_area_obj_factory_8cpp.md)


```C++
#include <Factory/alAreaObjFactory.h>

namespace al
{

template <typename T>
AreaObj* createAreaObjFunction( const char* name )
{
        return new T( name );
}

const NameToAreaObjCreator staticd( sAreaObjFactoryEntries )[] = {
        { "AudioEffectChangeArea", createAreaObjFunction<AreaObj> },
        { "AudioVolumeSettingArea", nullptr },
        { "BgmChangeArea", createAreaObjFunction<AreaObj> },
        { "CameraArea", nullptr },
        { "CameraOriginArea", createAreaObjFunction<AreaObj> },
        { "CameraWaveArea", createAreaObjFunction<AreaObj> },
        { "ChangeCoverArea", nullptr },
        { "DeathArea", createAreaObjFunction<AreaObj> },
        { "EnablePropellerFallCameraArea", createAreaObjFunction<AreaObj> },
        { "FogArea", createAreaObjFunction<AreaObj> },
        { "FogAreaCameraPos", createAreaObjFunction<AreaObj> },
        { "FootPrintFollowPosArea", createAreaObjFunction<AreaObj> },
        { "InvalidatePropellerCameraArea", createAreaObjFunction<AreaObj> },
        { "KinopioHouseExitArea", createAreaObjFunction<AreaObj> },
        { "LightArea", createAreaObjFunction<AreaObj> },
        { "ObjectChildArea", nullptr },
        { "PlayerAlongWallArea", createAreaObjFunction<AreaObj> },
        { "PlayerControlOffArea", createAreaObjFunction<AreaObj> },
        { "PlayerInclinedControlArea", createAreaObjFunction<AreaObj> },
        { "PlayerRestrictedPlane", nullptr },
        { "PlayerWidenStickXSnapArea", createAreaObjFunction<AreaObj> },
        { "PresentMessageArea", createAreaObjFunction<AreaObj> },
        { "SoundEmitArea", nullptr },
        { "SpotLightArea", nullptr },
        { "StickFixArea", createAreaObjFunction<AreaObj> },
        { "StickSnapOffArea", createAreaObjFunction<AreaObj> },
        { "SwitchKeepOnArea", nullptr },
        { "SwitchOnArea", nullptr },
        { "ViewCtrlArea", createAreaObjFunction<AreaObj> },
        { "WaterArea", createAreaObjFunction<AreaObj> },
        { "WaterFallArea", createAreaObjFunction<AreaObj> },
        { "WaterFlowArea", createAreaObjFunction<AreaObj> },
        { "GhostPlayerArea", createAreaObjFunction<AreaObj> },
        { "Guide3DArea", createAreaObjFunction<AreaObj> },
        { "MessageArea", nullptr },
        { "BugFixBalanceTruckArea", createAreaObjFunction<AreaObj> } };

} // namespace al
```


