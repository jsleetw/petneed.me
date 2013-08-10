package me.petneed.android.view;

import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.util.AttributeSet;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.ImageView;
import android.widget.TextView;
import com.googlecode.androidannotations.annotations.Click;
import com.googlecode.androidannotations.annotations.EViewGroup;
import com.googlecode.androidannotations.annotations.ViewById;
import com.koushikdutta.ion.Ion;
import me.petneed.android.R;
import me.petneed.android.model.Animal;
import me.petneed.android.model.DataManager;

@EViewGroup(R.layout.animal_view_dialog)
public class AnimalDialogView extends FrameLayout {



	@ViewById(R.id.dlg_animal_image)
	protected ImageView img;
	@ViewById(R.id.dlg_animal_name)
	protected TextView name;
    @ViewById(R.id.dlg_animal_detail)
    protected TextView note;
    @ViewById(R.id.dlg_animal_settle)
    protected TextView settlement;
    @ViewById(R.id.dlg_animal_btn_call)
    protected Button btnCall;

    public Animal getItem() {
        return mItem;
    }

    public void setItem(Animal mItem) {
        this.mItem = mItem;
    }

    private Animal mItem;


	public AnimalDialogView(Context context) {
		super(context);
		init();
	}

	public AnimalDialogView(Context context, AttributeSet attrs) {
		super(context, attrs);
		init();
	}

	public AnimalDialogView(Context context, AttributeSet attrs, int defStyle) {
		super(context, attrs, defStyle);
		init();
	}
	
	private void init() {
		
	}

    @Click(R.id.dlg_animal_btn_call)
    void btnCallClicked(){

        Intent intentDial = new Intent(Intent.ACTION_DIAL, Uri.parse("tel:" + getItem().getPhone().replaceAll("[-]","")));
        if (this.getContext() != null)
            this.getContext().startActivity(intentDial);
    }

    public void bind(final Animal item) {
        setItem(item);

//        Ion.with(img)
//                .placeholder(R.drawable.empty_img)
//                .load(DataManager.STATIC_END_POINT+item.getImage_file());
        Ion.with(img)
                .placeholder(R.drawable.empty_img)
                .load(DataManager.STATIC_END_POINT+item.getImageFileThumb());
        name.setText(item.getName());
        btnCall.setText(item.getPhone());
        note.setText(item.getNote());
        settlement.setText(item.getResettlement());
    }




}
