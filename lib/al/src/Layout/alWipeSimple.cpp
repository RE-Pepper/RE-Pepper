#include <Layout/alWipeSimple.h>
#include <Nerve/alNerveFunction.h>

namespace al
{

namespace NrvWipeSimple
{

NERVE_DEF( WipeSimple, Close )
NERVE_DEF( WipeSimple, Wait )
NERVE_DEF( WipeSimple, Open )

} // namespace NrvWipeSimple

WipeSimple::WipeSimple( const char* name, const char* archive, const LayoutInitInfo& info, const char* suffix )
    : LayoutActor( name ), _30( -1 )
{
        initLayoutActor( this, info, archive, suffix );
        initNerve( &NrvWipeSimple::Close );
}

void WipeSimple::appear()
{
        LayoutActor::appear();
}

void WipeSimple::exeClose()
{
        if ( !isFirstStep( this ) && isActionEnd( this ) )
                setNerve( this, &NrvWipeSimple::Wait );
}

void WipeSimple::exeWait()
{
        if ( isFirstStep( this ) )
                startAction( this, "Wait" );
}

#ifdef NON_MATCHING

// float math
void WipeSimple::exeOpen()
{
        if ( isFirstStep( this ) )
                setActionFrameRate( this, _30 < 1 ? 1.0 : getActionFrameMax( this ) / _30 );

        if ( isActionEnd( this ) )
                kill();
}
#endif

} // namespace al
