

# File alAreaObjFactory.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Factory**](dir_9d6e65e3d9c59adcbf76328d50237b6e.md) **>** [**alAreaObjFactory.cpp**](al_area_obj_factory_8cpp.md)

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


