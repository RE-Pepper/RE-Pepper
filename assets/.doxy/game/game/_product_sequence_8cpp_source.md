

# File ProductSequence.cpp

[**File List**](files.md) **>** [**Game**](dir_c33286056d2acf479cd8641ef845fec1.md) **>** [**src**](dir_d858f423bf5825f9a3db826b6a54a3cc.md) **>** [**Sequence**](dir_adde3a84bdb9ef9ce29831a9adedd06e.md) **>** [**ProductSequence.cpp**](_product_sequence_8cpp.md)

[Go to the documentation of this file](_product_sequence_8cpp.md)


```C++
#include "Sequence/ProductSequence.h"

#include <Nerve/alNerve.h>
#include <Nerve/alNerveFunction.h>

#include "Sequence/ProductStateCourseSelect.h"
#include "Sequence/ProductStateStage.h"

namespace NrvProductSequence
{

NERVE_DEF( ProductSequence, Title )
NERVE_DEF( ProductSequence, Opening )
NERVE_DEF( ProductSequence, CourseSelect )
NERVE_DEF( ProductSequence, Stage )
NERVE_DEF( ProductSequence, KinopioHouse )
NERVE_DEF( ProductSequence, MysteryBox )
NERVE_DEF( ProductSequence, Ending )
NERVE_DEF( ProductSequence, GameOverRoom )
NERVE_DEF( ProductSequence, Unk1 )

} // namespace NrvProductSequence

ProductSequence::ProductSequence( const char* name )
    : Sequence( name ), mStageStartParam( nullptr ), _14C( nullptr ), _150( nullptr ), mWipeKeeper( nullptr ),
      _158( nullptr ), _15C( nullptr ), mStateTitle( nullptr ), mStateOpening( nullptr ),
      mStateCourseSelect( nullptr ), mStateStage( nullptr ), mStateKinopioHouse( nullptr ),
      mStateMysteryBox( nullptr ), mStateEnding( nullptr ), mStateGameOverRoom( nullptr ), _180( nullptr ),
      _184( nullptr ), _188( nullptr ), _18C( nullptr ), _190( nullptr )
{
}

#ifdef NON_MATCHING
void ProductSequence::init()
{
} // needed for vtable

#endif

extern "C" bool fn_0025ba7c( const char* );

void ProductSequence::exeTitle()
{
        if ( al::updateNerveState( this ) )
        {
                if ( fn_0025ba7c( "オープニング実行" ) )
                        al::setNerve( this, &NrvProductSequence::CourseSelect );
                else
                        al::setNerve( this, &NrvProductSequence::Opening );
        }
}

void ProductSequence::exeOpening()
{
        if ( al::updateNerveState( this ) )
                al::setNerve( this, &NrvProductSequence::CourseSelect );
}

void ProductSequence::exeKinopioHouse()
{
        if ( al::updateNerveState( this ) )
        {
                mStateCourseSelect->set_10( 4 );
                al::setNerve( this, &NrvProductSequence::CourseSelect );
        }
}

extern "C" bool fn_0025ddd0();

void ProductSequence::exeEnding()
{
        if ( al::updateNerveState( this ) )
        {
                if ( fn_0025ddd0() )
                        al::setNerve( this, &NrvProductSequence::Unk1 );
                else
                        al::setNerve( this, &NrvProductSequence::Title );
        }
}
```


