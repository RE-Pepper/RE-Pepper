#include <Execute/alExecuteDirector.h>
#include <Layout/alLayoutKit.h>

namespace al
{

LayoutKit::LayoutKit( FontHolder* fontHolder )
    : _0( nullptr ), mFontHolder( fontHolder ), mExecuteDirector( nullptr ), _C( nullptr ), _10( nullptr ),
      _14( nullptr )
{
}

void LayoutKit::createExecuteDirector( int p )
{
        mExecuteDirector      = new ExecuteDirector( p );
        mExecuteDirector->_18 = _14;
        mExecuteDirector->init();
}

} // namespace al
