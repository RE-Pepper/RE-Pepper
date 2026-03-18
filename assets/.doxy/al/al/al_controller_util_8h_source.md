

# File alControllerUtil.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Controller**](dir_7e131ebde053fe7d3351d1831517cd0c.md) **>** [**alControllerUtil.h**](al_controller_util_8h.md)

[Go to the documentation of this file](al_controller_util_8h.md)


```C++
#pragma once

#include <math/seadVector.h>

namespace al
{

bool isPadTrigger( int port, int mask );
bool isPadHold( int port, int mask );
bool isPadRelease( int port, int mask );

#define _T_BUTTON( BUTTON )                        \
        bool isPadTrigger##BUTTON( int port = 0 ); \
        bool isPadHold##BUTTON( int port = 0 );    \
        bool isPadRelease##BUTTON( int port = 0 );

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

#undef _T_BUTTON

#ifndef __CC_ARM
const sead::Vector2f& getLeftStick( int port = 0 );
#endif

} // namespace al
```


