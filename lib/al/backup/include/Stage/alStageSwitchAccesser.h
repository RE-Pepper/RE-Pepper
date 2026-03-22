#pragma once

#include <Placement/alPlacementInfo.h>
#include <Stage/alStageSwitchType.h>

namespace al
{

class StageSwitchAccesser
{
private:
        int mId;
        int mType;

public:
        int initWithPlacementInfo( StageSwitchType type1, const PlacementInfo& info, StageSwitchType type2 );

        bool isTypeKillDeadOn() const;
        int  fn_0024e734() const; // ?

public:
        StageSwitchAccesser();
};

} // namespace al
