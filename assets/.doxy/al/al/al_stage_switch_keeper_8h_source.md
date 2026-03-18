

# File alStageSwitchKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Stage**](dir_5b0b61705299d400abf6aff2e591c6a0.md) **>** [**alStageSwitchKeeper.h**](al_stage_switch_keeper_8h.md)

[Go to the documentation of this file](al_stage_switch_keeper_8h.md)


```C++
#pragma once

namespace al
{
class FunctorBase;
class ActorInitInfo;
class StageSwitchAccesser;

class StageSwitchKeeper
{
private:
        StageSwitchAccesser* mSwitches;
        int                  mSwitchCount;

public:
        StageSwitchAccesser* getStageSwitchAccesser( int type );

public:
        StageSwitchKeeper();
};

class IUseStageSwitch
{
public:
        virtual StageSwitchKeeper* getStageSwitchKeeper() const = 0;
        virtual void               initStageSwitchKeeper()      = 0;
};

void initStageSwitchAppear( IUseStageSwitch* p, const ActorInitInfo& info );
void initStageSwitchKill( IUseStageSwitch* p, const ActorInitInfo& info );
void initStageSwitchA( IUseStageSwitch* p, const ActorInitInfo& info );
void initStageSwitchB( IUseStageSwitch* p, const ActorInitInfo& info );

bool isOnSwitchA( IUseStageSwitch* p );

bool listenStageSwitchOnAppear( IUseStageSwitch* p, const FunctorBase& onFunctor, const FunctorBase& offFunctor );

} // namespace al
```


