

# File alJMapInfo.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Util**](dir_6175f94551b875091d51e8ae0816c221.md) **>** [**alJMapInfo.cpp**](al_j_map_info_8cpp.md)

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


