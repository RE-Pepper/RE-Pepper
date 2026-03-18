

# File alPlacementFunction.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Placement**](dir_b0784325fb1baab636da39c4657eec3c.md) **>** [**alPlacementFunction.h**](al_placement_function_8h.md)

[Go to the documentation of this file](al_placement_function_8h.md)


```C++
#pragma once

#include <Placement/alPlacementInfo.h>
#include <math/seadQuat.h>
#include <math/seadVector.h>

namespace al
{
class ActorInitInfo;

bool isPlaced( const ActorInitInfo& info );

bool tryGetArg( bool* out, const PlacementInfo& info, const char* argName );
bool tryGetArg( float* out, const PlacementInfo& info, const char* argName );
bool tryGetArg( int* out, const PlacementInfo& info, const char* argName );
#ifndef __CC_ARM
inline bool tryGetArg( bool* out, const ActorInitInfo& info, const char* argName )
{
        return tryGetArg( out, getPlacementInfo( info ), argName );
}

inline bool tryGetArg( float* out, const ActorInitInfo& info, const char* argName )
{
        return tryGetArg( out, getPlacementInfo( info ), argName );
}

inline bool tryGetArg( int* out, const ActorInitInfo& info, const char* argName )
{
        return tryGetArg( out, getPlacementInfo( info ), argName );
}
#endif
bool tryGetArg0( int* out, const PlacementInfo& info );
bool tryGetArg0( float* out, const ActorInitInfo& info );
bool tryGetArg1( float* out, const ActorInitInfo& info );
bool tryGetArg3( int* out, const ActorInitInfo& info );
bool tryGetStringArg( const char** out, const ActorInitInfo& info, const char* argName );
bool tryGetStringArg( const char** out, const PlacementInfo& info, const char* argName );

bool tryGetObjectName( const char** out, const ActorInitInfo& info );
bool tryGetObjectName( const char** out, const PlacementInfo& info );
bool isObjectName( const ActorInitInfo& info, const char* objectName );
bool isObjectName( const PlacementInfo& info, const char* objectName );

int calcLinkChildNum( const ActorInitInfo& info );

bool tryGetTrans( sead::Vector3f* out, const ActorInitInfo& info );
bool tryGetTrans( sead::Vector3f* out, const PlacementInfo& info );
bool tryGetQuat( sead::Quatf* out, const PlacementInfo& info );

bool isExistRail( const ActorInitInfo& info );
bool tryGetRailIter( PlacementInfo* out, const PlacementInfo& info );

bool        getLinksInfoByIndex( PlacementInfo* out, const ActorInitInfo& info, int index );
const char* getLinksActorObjectName( const ActorInitInfo& info, int index );

} // namespace al

namespace alPlacementFunction
{

int getClippingViewId( const al::PlacementInfo& info );

} // namespace alPlacementFunction
```


