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
