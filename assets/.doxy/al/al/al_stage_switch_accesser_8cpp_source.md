

# File alStageSwitchAccesser.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Stage**](dir_1105584207b8da44b58906e6f5240647.md) **>** [**alStageSwitchAccesser.cpp**](al_stage_switch_accesser_8cpp.md)

[Go to the documentation of this file](al_stage_switch_accesser_8cpp.md)


```C++
#include <Stage/alStageSwitchAccesser.h>

namespace al
{

StageSwitchAccesser::StageSwitchAccesser() : mId( -1 ), mType( 0 )
{
}

int StageSwitchAccesser::initWithPlacementInfo( StageSwitchType type1, const PlacementInfo& info, StageSwitchType type2 )
{
        const char* type1Name = getStageSwitchName( type1 );
        if ( mType > (int)type2 )
                type2 = (StageSwitchType)mType;
        mId   = -1;
        mType = type2;
        info.tryGetIntByKey( &mId, type1Name );
        return fn_0024e734();
}

bool StageSwitchAccesser::isTypeKillDeadOn() const
{
        return mType == StageSwitchType_Kill || mType == StageSwitchType_DeadOn;
}

int StageSwitchAccesser::fn_0024e734() const
{
        return ( mId >> 0x1f ) + 1;
} // ?

} // namespace al
```


