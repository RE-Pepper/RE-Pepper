#pragma once

#include <prim/seadSafeString.h>

namespace sead
{
class FileDevice;
}

namespace al
{

class FileLoader
{
private:
        u8 _0[ 0x30 ];

public:
        void loadArchive( const sead::SafeString& archive, sead::FileDevice* );

public:
        FileLoader( int );
};

} // namespace al
