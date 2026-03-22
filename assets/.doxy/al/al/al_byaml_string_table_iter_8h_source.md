

# File alByamlStringTableIter.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Yaml**](dir_4db20b6947036956387e84dab645aa7e.md) **>** [**alByamlStringTableIter.h**](al_byaml_string_table_iter_8h.md)

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


