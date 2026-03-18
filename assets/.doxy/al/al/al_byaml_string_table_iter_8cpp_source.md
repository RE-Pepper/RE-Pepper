

# File alByamlStringTableIter.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Yaml**](dir_a66705d5185d64e99b2223010bf5d935.md) **>** [**alByamlStringTableIter.cpp**](al_byaml_string_table_iter_8cpp.md)

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


