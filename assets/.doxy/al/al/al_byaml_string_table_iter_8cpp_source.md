

# File alByamlStringTableIter.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Yaml**](dir_88abf051c89dccbd64e4b1732f597ee0.md) **>** [**alByamlStringTableIter.cpp**](al_byaml_string_table_iter_8cpp.md)

[Go to the documentation of this file](al_byaml_string_table_iter_8cpp.md)


```C++
#include <Yaml/alByamlStringTableIter.h>
#include <cstring>

namespace al
{

int ByamlStringTableIter::findStringIndex( const char* str ) const
{
        int        low = 0, index = 0;
        int        high  = mHeader->stringAmount;
        const u32* table = getAddressTable();

        if ( high <= 0 )
                return -1;

        while ( high > low )
        {
                index   = ( low + high ) / 2;
                int res = std::strcmp( str, (const char*)&mData[ table[ index ] ] );
                if ( res < 0 )
                        high = index;
                else if ( res > 0 )
                        low = index + 1;
                if ( res == 0 )
                        return index;
        }

        return -1;
}

} // namespace al
```


