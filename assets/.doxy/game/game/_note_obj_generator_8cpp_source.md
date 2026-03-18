

# File NoteObjGenerator.cpp

[**File List**](files.md) **>** [**Game**](dir_c33286056d2acf479cd8641ef845fec1.md) **>** [**src**](dir_d858f423bf5825f9a3db826b6a54a3cc.md) **>** [**MapObj**](dir_9fb1f6495822aa302d379b21d455a7ad.md) **>** [**NoteObjGenerator.cpp**](_note_obj_generator_8cpp.md)

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


