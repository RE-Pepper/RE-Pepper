#pragma once

#include <MapObj/alMapObjActor.h>

class WalkerStateWander;
class WalkerStateChase;
class EnemyStateBlowDown;

class Togezo : public al::MapObjActor
{
private:
        WalkerStateWander*  mWanderState;
        WalkerStateChase*   mChaseState;
        EnemyStateBlowDown* mBlowDownState;

public:
        void exeWander();
        void exeTurn();
        void exeSearch();
        void exeChase();
        void exeAttack();
        void exeBlowDown();

public:
        virtual void init( const al::ActorInitInfo& info );

public:
        Togezo( const sead::SafeString& name );
};
