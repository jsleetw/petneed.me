package me.petneed.android;

import android.annotation.TargetApi;
import android.app.ActionBar;
import android.content.Context;
import android.os.Build;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentActivity;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Toast;
import com.googlecode.androidannotations.annotations.AfterViews;
import com.googlecode.androidannotations.annotations.Click;
import com.googlecode.androidannotations.annotations.EActivity;
import com.googlecode.androidannotations.annotations.ViewById;
import me.petneed.android.model.Animal;
import me.petneed.android.model.DataManager;
import me.petneed.android.view.AnimalDialogView;
import me.petneed.android.view.SectionFragment;

import java.util.ArrayList;
import java.util.HashMap;

@EActivity(R.layout.activity_main)
public class MainActivity extends FragmentActivity implements
        ActionBar.OnNavigationListener, DataManager.DataUpdatedListener {


    @ViewById(R.id.dlg_view_all)
    View dlgAll;
    @ViewById(R.id.dlg_view_animal_detail)
    AnimalDialogView dlgDetailView;
    DataManager dataManager = new DataManager(this);
    /**
     * The serialization (saved instance state) Bundle key representing the
     * current dropdown position.
     */
    private static final String STATE_SELECTED_NAVIGATION_ITEM = "selected_navigation_item";
    private ArrayList<String> typeList;

    //    @Override
//    protected void onCreate(Bundle savedInstanceState) {
//        super.onCreate(savedInstanceState);
//        setContentView(R.layout.activity_main);
//
//
//
//    }
//
    @AfterViews
    void afterCreate() {
        // Set up the action bar to show a dropdown list.
        final ActionBar actionBar = getActionBar();
        actionBar.setDisplayShowTitleEnabled(false);
        actionBar.setNavigationMode(ActionBar.NAVIGATION_MODE_LIST);

        DummyProgressFragment fragment = new DummyProgressFragment();
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.container, fragment).commit();
        dataManager.setListener(this);
        dataManager.initData();
    }

    /**
     * Backward-compatible version of {@link ActionBar#getThemedContext()} that
     * simply returns the {@link android.app.Activity} if
     * <code>getThemedContext</code> is unavailable.
     */
    @TargetApi(Build.VERSION_CODES.ICE_CREAM_SANDWICH)
    private Context getActionBarThemedContextCompat() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.ICE_CREAM_SANDWICH) {
            return getActionBar().getThemedContext();
        } else {
            return this;
        }
    }

    @Override
    public void onRestoreInstanceState(Bundle savedInstanceState) {
        // Restore the previously serialized current dropdown position.
        if (savedInstanceState.containsKey(STATE_SELECTED_NAVIGATION_ITEM)) {
            getActionBar().setSelectedNavigationItem(
                    savedInstanceState.getInt(STATE_SELECTED_NAVIGATION_ITEM));
        }
    }

    @Override
    public void onSaveInstanceState(Bundle outState) {
        // Serialize the current dropdown position.
        outState.putInt(STATE_SELECTED_NAVIGATION_ITEM, getActionBar()
                .getSelectedNavigationIndex());
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    HashMap<String, SectionFragment> frags = new HashMap<String, SectionFragment>();

    @Override
    public boolean onNavigationItemSelected(int position, long id) {

        // When the given dropdown item is selected, show its contents in the
        // container view.
        SectionFragment fragment;

        if (frags.get(typeList.get(position)) == null) {
            fragment = new SectionFragment();
            Bundle args = new Bundle();
            args.putInt(SectionFragment.ARG_SECTION_NUMBER, position + 1);
            args.putString(SectionFragment.ARG_TYPE, typeList.get(position));
            fragment.setDataManager(dataManager);
            fragment.setArguments(args);
        } else {
            fragment = frags.get(typeList.get(position));
        }
        getSupportFragmentManager().beginTransaction()
                .replace(R.id.container, fragment).commit();
        return true;
    }

    @Override
    public void dataUpdated(DataManager.ApiType code) {
        final ActionBar actionBar = getActionBar();
        if (actionBar != null) {
            String[] types = new String[dataManager.getTypeCount()];
            typeList = new ArrayList<String>(dataManager.getTypes());
            typeList.toArray(types);


            // Set up the dropdown list navigation in the action bar.
            actionBar.setListNavigationCallbacks(
                    // Specify a SpinnerAdapter to populate the dropdown list.
                    new ArrayAdapter<String>(getActionBarThemedContextCompat(),
                            android.R.layout.simple_list_item_1,
                            android.R.id.text1, types), this);
        }
    }

    @Override
    public void dataUpdateFailed(DataManager.ApiType code) {
        Toast.makeText(this, "Get Data Failed Q_Q...", Toast.LENGTH_LONG).show();
    }

    @Override
    public void dataDetailView(Object obj) {
        dlgAll.setVisibility(View.VISIBLE);
        dlgDetailView.bind((Animal) obj);
    }

    @Click(R.id.dlg_view_all)
    void dlgClicked() {
        dlgAll.setVisibility(View.GONE);
    }

    @Override
    public void onBackPressed() {
        if (dlgAll.getVisibility() == View.VISIBLE) {
            dlgAll.setVisibility(View.GONE);
        } else {
            super.onBackPressed();
        }
    }

    public class DummyProgressFragment extends Fragment {


        public DummyProgressFragment() {
        }

        @Override
        public View onCreateView(LayoutInflater inflater, ViewGroup container,
                                 Bundle savedInstanceState) {
            View rootView = inflater.inflate(R.layout.fragment_main_progress,
                    container, false);

            return rootView;
        }

    }
}
