

# File alControllerUtil.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Controller**](dir_d067c0de001f0fe841ce7f520c46c4e3.md) **>** [**alControllerUtil.cpp**](al_controller_util_8cpp.md)

[Go to the documentation of this file](al_controller_util_8cpp.md)


```C++
#pragma once

#include <Controller/alControllerUtil.h>
#include <controller/seadControllerMgr.h>

namespace al
{

extern "C" const u32* fn_0024edd8();

bool isPadTrigger( int port, int mask )
{ // likely a fakematch
        int        masktemp = mask;
        int        porttemp = port;
        const u32* maskPtr  = fn_0024edd8();

        if ( !maskPtr )
        {
                sead::Controller* controller = sead::ControllerMgr::instance()->getController( porttemp );
                maskPtr                      = controller ? controller->getTrigMaskPtr() : 0;
        }
        return *maskPtr & masktemp;
}

#define _T_BUTTON( BUTTON )                                                           \
        bool isPadTrigger##BUTTON( int port )                                         \
        {                                                                             \
                return isPadTrigger( port, 1 << sead::Controller::cPadIdx_##BUTTON ); \
        }                                                                             \
        bool isPadHold##BUTTON( int port )                                            \
        {                                                                             \
                return isPadHold( port, 1 << sead::Controller::cPadIdx_##BUTTON );    \
        }                                                                             \
        bool isPadRelease##BUTTON( int port )                                         \
        {                                                                             \
                return isPadRelease( port, 1 << sead::Controller::cPadIdx_##BUTTON ); \
        }

_T_BUTTON( A );
_T_BUTTON( B );
_T_BUTTON( X );
_T_BUTTON( Y );
_T_BUTTON( Home );
_T_BUTTON( Minus );
_T_BUTTON( Start );
_T_BUTTON( Select );
_T_BUTTON( L );
_T_BUTTON( R );
_T_BUTTON( Touch );
_T_BUTTON( Up );
_T_BUTTON( Down );
_T_BUTTON( Left );
_T_BUTTON( Right );
_T_BUTTON( LeftStickUp );
_T_BUTTON( LeftStickDown );
_T_BUTTON( LeftStickLeft );
_T_BUTTON( LeftStickRight );

#undef _T_BUTTON

} // namespace al
```


