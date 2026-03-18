

# File alByamlStringTableIter.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Yaml**](dir_ead735227c22214cb122acbd07613fdc.md) **>** [**alByamlStringTableIter.h**](al_byaml_string_table_iter_8h.md)

[Go to the documentation of this file](al_byaml_string_table_iter_8h.md)


```C++
#pragma once

#include <Yaml/alByamlData.h>

namespace al
{

class ByamlStringTableIter
{
private:
        struct Header
        {
                const ByamlDataType type : 8;
                const u32           stringAmount : 24;
        };

        union
        {
                const u8*     mData;
                uintptr_t     mDataPtr;
                const Header* mHeader;
        };

public:
        ByamlStringTableIter( const u8* data ) : mData( data )
        {
        }

        const u32* getAddressTable() const
        {
                return reinterpret_cast<u32*>( mDataPtr + sizeof( mDataPtr ) );
        }

        int findStringIndex( const char* str ) const;
};

} // namespace al
```


