

# File alJMapInfo.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Util**](dir_4478c2a5592b6f930f15f50e4557300c.md) **>** [**alJMapInfo.cpp**](al_j_map_info_8cpp.md)

[Go to the documentation of this file](al_j_map_info_8cpp.md)


```C++
#include <Util/alJMapInfo.h>

JMapInfo::JMapInfo() : mData( nullptr ), mName( "Undifined" )
{
}

bool JMapInfo::attach( const void* data )
{
        if ( !data )
                return false;

        mData = JMapData::fromData( data );
        return true;
}
```


