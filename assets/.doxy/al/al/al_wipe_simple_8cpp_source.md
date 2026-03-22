

# File alWipeSimple.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Layout**](dir_1957e6da08be5c5351242f28ef490eb7.md) **>** [**alWipeSimple.cpp**](al_wipe_simple_8cpp.md)

[Go to the documentation of this file](al_wipe_simple_8cpp.md)


```C++
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
```


