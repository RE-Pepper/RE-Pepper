

# File NoteObjGenerator.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**MapObj**](dir_d5af9f6f62d27d9e3db1b7ff0fb6c0e1.md) **>** [**NoteObjGenerator.cpp**](_note_obj_generator_8cpp.md)

[Go to the documentation of this file](_note_obj_generator_8cpp.md)


```C++
#include "MapObj/NoteObjGenerator.h"

#include <LiveActor/alLiveActorFunction.h>
#include <Nerve/alNerve.h>
#include <Nerve/alNerveActionCtrl.h>
#include <Nerve/alNerveFunction.h>
#include <Stage/alStageSwitchKeeper.h>

#include "MapObj/NoteObj.h"

static alNerveFunction::NerveActionCollector sCollector;

namespace NrvNoteObjGenerator
{

NERVEACTION_DEF( NoteObjGenerator, Wait )
NERVEACTION_DEF( NoteObjGenerator, Move )
NERVEACTION_DEF( NoteObjGenerator, Disappear )
NERVEACTION_DEF( NoteObjGenerator, Success )

} // namespace NrvNoteObjGenerator

NoteObjGenerator::NoteObjGenerator( const sead::SafeString& name )
    : MapObjActor( name ), mNoteObjGroup( nullptr ), _64( nullptr ), _68( 20 ), _6C( 200 ), _70( nullptr ),
      _74( 180 ), _78( false ), _7C( 0 ), _80( nullptr ), _84( false )
{
}

extern "C" void fn_00270fc4( al::LiveActor*, float, int ); // MtxConnector (?)
extern "C" void fn_001d581c();

void NoteObjGenerator::exeWait()
{
        if ( al::isOnSwitchA( this ) )
        {
                al::invalidateClipping( this );
                al::showModel( this );
                fn_00270fc4( this, 70.0, 1 );
                al::startAction( this, "Wait" );
                fn_001d581c();
                al::startNerveAction( this, "Move" );
        }
}

void NoteObjGenerator::exeSuccess()
{
        if ( al::isGreaterEqualStep( this, 12 ) )
                kill();
}
```


