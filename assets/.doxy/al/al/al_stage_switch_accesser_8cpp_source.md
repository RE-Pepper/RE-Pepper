

# File alStageSwitchAccesser.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Stage**](dir_5711be3bb70244779513d118f4c8331f.md) **>** [**alStageSwitchAccesser.cpp**](al_stage_switch_accesser_8cpp.md)

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


