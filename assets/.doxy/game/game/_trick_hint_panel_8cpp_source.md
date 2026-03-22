

# File TrickHintPanel.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**MapObj**](dir_d5af9f6f62d27d9e3db1b7ff0fb6c0e1.md) **>** [**TrickHintPanel.cpp**](_trick_hint_panel_8cpp.md)

[Go to the documentation of this file](_trick_hint_panel_8cpp.md)


```C++
#include "MapObj/TrickHintPanel.h"

#include <LiveActor/alActorActionKeeper.h>
#include <LiveActor/alActorInitUtil.h>
#include <LiveActor/alLiveActorFunction.h>
#include <LiveActor/alSensorMsg.h>
#include <Nerve/alNerve.h>
#include <Nerve/alNerveFunction.h>
#include <Nerve/alNerveStateBase.h>

namespace NrvTrickHintPanel
{

NERVE_DEF( TrickHintPanel, Wait );
NERVE_DEF( TrickHintPanel, On );
NERVE_DEF( TrickHintPanel, nrv3 );
NERVE_DEF( TrickHintPanel, Off );

} // namespace NrvTrickHintPanel

TrickHintPanel::TrickHintPanel( const sead::SafeString& name )
    : MapObjActor( name ), _96( 0 ), mPlayedSound( false )
{
}

extern "C" u32 fn_002278CC( al::LiveActor* actor, char* str );

void TrickHintPanel::init( const al::ActorInitInfo& info )
{
        al::initActor( this, info );
        al::initNerve( this, &NrvTrickHintPanel::Wait, 0 );
        _96 = fn_002278CC( this, "" );
        makeActorAppeared();
}

bool TrickHintPanel::receiveMsg( u32 msg, al::HitSensor* other, al::HitSensor* me )
{
        if ( al::isMsgPlayerFloorTouch( msg ) )
        {
                if ( al::isNerve( this, &NrvTrickHintPanel::Wait ) )
                {
                        al::setNerve( this, &NrvTrickHintPanel::On );
                        return true;
                }

                if ( al::isNerve( this, &NrvTrickHintPanel::nrv3 ) )
                {
                        al::setNerve( this, &NrvTrickHintPanel::nrv3 );
                        return true;
                }
        }
        return false;
}

void TrickHintPanel::exeWait()
{
}

extern "C" int fn_0026A9B8( u32 );
extern "C" int fn_0026AA60( u32 );
extern "C" int fn_002786F4();

#ifdef NON_MATCHING

// inline nops
void TrickHintPanel::exeOn()
{
        if ( !mPlayedSound )
        {
                al::startHitReactionStart( this );
                mPlayedSound = true;
        }
        al::startHitReaction( this, "オン" ); // "オン" -> On
        fn_0026A9B8( _96 );
        al::invalidateClipping( this );
        al::setNerve( this, &NrvTrickHintPanel::nrv3 );
}
#endif

void TrickHintPanel::exenrv3()
{
        if ( !fn_002786F4() || al::isGreaterStep( this, 20 ) )
                al::setNerve( this, &NrvTrickHintPanel::Off );
}

void TrickHintPanel::exeOff()
{
        if ( fn_002786F4() )
        {
                fn_0026AA60( _96 );
                al::validateClipping( this );
                al::setNerve( this, &NrvTrickHintPanel::Wait );
        }
}
```


