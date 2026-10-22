#include <Util/alJMapInfo.h>

namespace al
{

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

} // namespace al
