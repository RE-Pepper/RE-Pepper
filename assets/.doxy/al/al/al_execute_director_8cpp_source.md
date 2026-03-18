

# File alExecuteDirector.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Execute**](dir_f4cdcb9032257672e779ef34d2d06033.md) **>** [**alExecuteDirector.cpp**](al_execute_director_8cpp.md)

[Go to the documentation of this file](al_execute_director_8cpp.md)


```C++
#include <Execute/alExecuteDirector.h>
#include <Execute/alExecuteOrder.h>
#include <Execute/alExecuteRequestKeeper.h>
#include <Execute/alExecuteTableHolderDraw.h>
#include <Execute/alExecuteTableHolderUpdate.h>

namespace al
{

ExecuteDirector::ExecuteDirector( int p )
    : _0( p ), mUpdateTable( nullptr ), mDrawTableAmount( 0 ), mDrawTables( nullptr ),
      mRequestKeeper( nullptr ), _14( 0 ), _18( 0 )
{
}

static const ExecuteOrder split( sUpdateExecuteOrder ) = { "クリッピング", "Execute", 1, "システム" };

static const ExecuteOrder split( sDraw0ExecuteOrder ) = { "空", "ActorModelDraw", 8, "地形" };
static const ExecuteOrder split( sDraw1ExecuteOrder ) = { "２Ｄエンドロールテキスト", "LayoutDraw", 64, "レイアウト" };
static const ExecuteOrder split( sDraw2ExecuteOrder ) = { "固定地形", "ActorModelDrawModelCache", 32, "地形" };
static const ExecuteOrder split( sDraw3ExecuteOrder ) = { "コリジョン地形", "ActorModelDraw", 128, "地形" };
static const ExecuteOrder split( sDraw4ExecuteOrder ) = { "２Ｄアイコン", "LayoutDraw", 128, "レイアウト" };
static const ExecuteOrder split( sDraw5ExecuteOrder ) = { "２Ｄベース", "LayoutDraw", 128, "レイアウト" };
static const ExecuteOrder split( sDraw6ExecuteOrder ) = { "２Ｄポーズ", "LayoutDraw", 8, "レイアウト" };
static const ExecuteOrder split( sDraw7ExecuteOrder ) = { "２Ｄベース（下画面）", "LayoutDrawBottom", 8, "レイアウト" };
static const ExecuteOrder split( sDraw8ExecuteOrder ) = { "アイテムストックモデル", "ActorModelDraw", 32, "アイテム" };
static const ExecuteOrder split( sDraw9ExecuteOrder ) = { "２Ｄポーズ（下画面）", "LayoutDrawBottom", 8, "レイアウト" };

#ifdef NON_MATCHING

// small instruction swap in operator new[]
void ExecuteDirector::init()
{
        mUpdateTable = new ExecuteTableHolderUpdate;
        mUpdateTable->init( &sUpdateExecuteOrder, 58 );
        mDrawTableAmount = 10;
        mDrawTables      = new ExecuteTableHolderDraw*[ mDrawTableAmount ];

        for ( int i = 0; i < mDrawTableAmount; i++ )
        {
                ExecuteTableHolderDraw* newDrawTable = new ExecuteTableHolderDraw;
                mDrawTables[ i ]                     = newDrawTable;
                if ( _14 )
                        newDrawTable->_48 = _14;
                if ( _18 )
                        newDrawTable->_4C = _18;
        }

        mDrawTables[ 0 ]->init( "３Ｄ（空）", &sDraw0ExecuteOrder, 4 );
        mDrawTables[ 1 ]->init( "２Ｄエンドロールテキスト（上画面）", &sDraw1ExecuteOrder, 1 );
        mDrawTables[ 2 ]->init( "３Ｄ（固定地形）", &sDraw2ExecuteOrder, 2 );
        mDrawTables[ 3 ]->init( "３Ｄ（上画面）", &sDraw3ExecuteOrder, 32 );
        mDrawTables[ 4 ]->init( "２Ｄアイコン（上画面）", &sDraw4ExecuteOrder, 1 );
        mDrawTables[ 5 ]->init( "２Ｄベース（上画面）", &sDraw5ExecuteOrder, 5 );
        mDrawTables[ 6 ]->init( "２Ｄ（上画面）", &sDraw6ExecuteOrder, 10 );
        mDrawTables[ 7 ]->init( "２Ｄベース（下画面）", &sDraw7ExecuteOrder, 2 );
        mDrawTables[ 8 ]->init( "３Ｄ（アイテムストック）", &sDraw8ExecuteOrder, 1 );
        mDrawTables[ 9 ]->init( "２Ｄ（下画面）", &sDraw9ExecuteOrder, 9 );

        mRequestKeeper = new ExecuteRequestKeeper( _0 );
}
#endif

void ExecuteDirector::createExecutorListTable()
{
        mUpdateTable->createExecutorListTable();
        for ( int i = 0; i < mDrawTableAmount; i++ )
                mDrawTables[ i ]->createExecutorListTable();
}

void ExecuteDirector::registerUser( al::IUseExecutor* p, const char* str )
{
        mUpdateTable->tryRegisterUser( p, str );
        for ( int i = 0; i < mDrawTableAmount; i++ )
                mDrawTables[ i ]->tryRegisterUser( p, str );
}

void ExecuteDirector::registerFunctor( const al::FunctorBase& base, const char* str )
{
        mUpdateTable->tryRegisterFunctor( base, str );
        for ( int i = 0; i < mDrawTableAmount; i++ )
                mDrawTables[ i ]->tryRegisterFunctor( base, str );
}

void ExecuteDirector::registerFunctorDraw( const al::FunctorBase& base, const char* str )
{
        for ( int i = 0; i < mDrawTableAmount; i++ )
                mDrawTables[ i ]->tryRegisterFunctor( base, str );
}

} // namespace al
```


